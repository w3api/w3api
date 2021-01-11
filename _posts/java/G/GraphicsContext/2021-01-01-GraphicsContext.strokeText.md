---
title: GraphicsContext.strokeText()
permalink: Java/GraphicsContext/strokeText
date: 2021-01-11
key: JavaJava.G.GraphicsContext
category: java
tags: ['java se', 'javafx.scene.canvas', 'javafx.graphics', 'metodo java', 'JavaFX 2.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GraphicsContext.metodos valor="strokeText" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void strokeText(String text, double x, double y)
public void strokeText(String text, double x, double y, double maxWidth)
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_dato parametro="String text" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **double y**,  {% include w3api/param_description.html metodo=_dato parametro="double y" %}
* **double maxWidth**,  {% include w3api/param_description.html metodo=_dato parametro="double maxWidth" %}

## Clase Padre
[GraphicsContext](/Java/GraphicsContext/)

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
