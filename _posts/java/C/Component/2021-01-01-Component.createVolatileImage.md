---
title: Component.createVolatileImage()
permalink: /Java/Component/createVolatileImage/
date: 2021-01-11
key: Java.C.Component
category: Java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Component.metodos valor="createVolatileImage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public VolatileImage createVolatileImage(int width, int height)
public VolatileImage createVolatileImage(int width, int height, ImageCapabilities caps) throws AWTException
~~~

## Parámetros
* **ImageCapabilities caps**,  {% include w3api/param_description.html metodo=_dato parametro="ImageCapabilities caps" %}
* **int height**,  {% include w3api/param_description.html metodo=_dato parametro="int height" %}
* **int width**,  {% include w3api/param_description.html metodo=_dato parametro="int width" %}

## Excepciones
[AWTException](/Java/AWTException/)

## Clase Padre
[Component](/Java/Component/)

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
