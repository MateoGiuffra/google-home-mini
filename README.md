# Flask Web Opener

Este proyecto es una pequeña aplicación Flask que abre una URL en el navegador del sistema cuando se accede a la ruta `/abrir`.

---

Por defecto abre YouTube si no se indica el parámetro `url` en la consulta.

---

## ¿Para qué lo hice?

Junto con **IFTTT**, logré que al decirle al Google Home Mini:  
**"Okay Google, activate YouTube"**,  
se abra una pestaña nueva de YouTube en mi navegador.

---

### Caso borde

- Si el navegador está cerrado, **igual funciona**, abriéndolo directamente en una nueva pestaña.

---

### ¿Qué navegador se usa?

El navegador que tengas configurado como **predeterminado** en tu sistema operativo.

### ¿Cómo probarlo?

Necesitás tu dirección **IP local** y reemplazarla donde dice `IP` en la URL.  
Luego, hacé una petición GET (puede ser desde el navegador o herramientas como Postman o curl).

Ejemplo:

```bash
http://IP:5000/abrir?url=https://youtube.com
```

> Si no pasás el parámetro `url`, abrirá YouTube por defecto.
