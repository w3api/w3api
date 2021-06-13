---
title: PixelWriter.setColor()
permalink: /Java/PixelWriter/setColor/
date: 2021-01-11
key: Java.P.PixelWriter
category: java
tags: ['java se', 'javafx.scene.image', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PixelWriter.metodos valor="setColor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setColor(int x, int y, Color c)
~~~

## Parámetros
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **Color c**,  {% include w3api/param_description.html metodo=_dato parametro="Color c" %}
* **int y**,  {% include w3api/param_description.html metodo=_dato parametro="int y" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PixelWriter](/Java/PixelWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
