#include <cstdlib>
#include <glut.h>

float rotationAngle = 0.0f;

void desenhaEstrelas() {
    glPointSize(1.0f);
    glBegin(GL_POINTS);
    glColor3f(1.0f, 1.0f, 1.0f); // Branco
    for (int i = 0; i < 1000; ++i) {
        float x = static_cast<float>(rand()) / RAND_MAX * 10.0f - 5.0f; // Coordenada random x
        float y = static_cast<float>(rand()) / RAND_MAX * 10.0f - 5.0f; // Coordenada random y 
        float z = static_cast<float>(rand()) / RAND_MAX * 10.0f - 5.0f; // Coordenada random z
        glVertex3f(x, y, z); // Plota a estrela
    }
    glEnd();
}

void desenhaArwing() {
    // Fuselagem
    glBegin(GL_TRIANGLES);
    glColor3f(0.7f, 0.7f, 0.7f);
    glVertex3f(0.0f, 0.0f, 1.8f);
    glVertex3f(0.0f, 0.3f, 0.0f);
    glVertex3f(0.3f, 0.0f, 0.0f);

    glVertex3f(0.0f, 0.0f, 1.8f);
    glVertex3f(0.0f, 0.3f, 0.0f);
    glVertex3f(-0.3f, 0.0f, 0.0f);

    glVertex3f(0.0f, 0.0f, 1.8f);
    glVertex3f(0.0f, 0.2f, -0.3f);
    glVertex3f(0.0f, 0.2f, 0.0f);
    glEnd();

    // Asinha esquerda
    glBegin(GL_TRIANGLES);
    glColor3f(0.26f, 0.26f, 1.0f);
    glVertex3f(-0.4f, -0.3f, 0.6f);
    glVertex3f(-0.7f, 0.8f, -1.0f);
    glVertex3f(-0.5f, 0.0f, 0.0f);

    glVertex3f(-0.4f, -0.3f, 0.6f);
    glVertex3f(-0.7f, 0.8f, -1.0f);
    glVertex3f(-0.5f, 0.0f, 0.0f);
    glEnd();

    // Asinha direita
    glBegin(GL_TRIANGLES);
    glColor3f(0.26f, 0.26f, 1.0f);
    glVertex3f(0.4f, -0.3f, 0.6f);
    glVertex3f(0.7f, 0.8f, -1.0f);
    glVertex3f(0.5f, 0.0f, 0.0f);

    glVertex3f(0.4f, -0.3f, 0.6f);
    glVertex3f(0.7f, 0.8f, -1.0f);
    glVertex3f(0.5f, 0.0f, 0.0f);
    glEnd();

    // Asa esquerda
    glBegin(GL_TRIANGLES);
    glColor3f(0.7f, 0.7f, 0.7f);
    glVertex3f(-1.7f, -0.4f, -1.4f);
    glVertex3f(-0.7f, 0.0f, 0.0f);
    glVertex3f(-0.5f, -0.2f, -0.1f);

    glVertex3f(-1.7f, -0.4f, -1.4f);
    glVertex3f(-0.7f, 0.0f, 0.0f);
    glVertex3f(-0.5f, -0.2f, -0.1f);
    glEnd();

    // Asa direita
    glBegin(GL_TRIANGLES);
    glColor3f(0.7f, 0.7f, 0.7f);
    glVertex3f(1.7f, -0.4f, -1.4f);
    glVertex3f(0.7f, 0.0f, 0.0f);
    glVertex3f(0.5f, -0.2f, -0.1f);

    glVertex3f(1.7f, -0.4f, -1.4f);
    glVertex3f(0.7f, 0.0f, 0.0f);
    glVertex3f(0.5f, -0.2f, -0.1f);
    glEnd();
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();
    gluLookAt(0.0f, 0.0f, 5.0f, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f);
    glRotatef(30.0f, 1.0f, 0.0f, 0.0f); // rotação no ângulo y
    glRotatef(rotationAngle, 0.0f, 1.0f, 0.0f); // aplica rotação
    desenhaEstrelas(); // desenha estrelas no background a cada chamado
    desenhaArwing(); // desenha a nave
    glFlush();
    glutSwapBuffers();
}

void update(int value) {
    rotationAngle += 1.0f; // atualiza angulo de rotação
    if (rotationAngle > 360.0f) {
        rotationAngle -= 360.0f;
    }
    glutPostRedisplay();
    glutTimerFunc(16, update, 0);
}

void reshape(int width, int height) {
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0f, (float)width / height, 0.1f, 100.0f);
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH); // 2 buffers
    glutInitWindowSize(800, 600);
    glutCreateWindow("Arwing (Starfox)");
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutTimerFunc(0, update, 0); // inicia o timer
    glutMainLoop();
    return 0;
}
