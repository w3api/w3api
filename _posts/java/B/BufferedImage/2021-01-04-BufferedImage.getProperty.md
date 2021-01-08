---
title: BufferedImage.getProperty()
permalink: Java/BufferedImage/getProperty
date: 2021-01-04
key: JavaJava.B.BufferedImage
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BufferedImage.metodos valor="getProperty" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getProperty(String name)
public Object getProperty(String name, ImageObserver observer)
~~~

## Parámetros
* **ImageObserver observer**,  {% include w3api/param_description.html metodo=_data parametro="ImageObserver observer" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BufferedImage](/Java/BufferedImage/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BufferedImage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
