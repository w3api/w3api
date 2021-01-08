---
title: StyleContext.writeAttributes()
permalink: Java/StyleContext/writeAttributes
date: 2021-01-04
key: JavaJava.S.StyleContext
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleContext.metodos valor="writeAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void writeAttributes(ObjectOutputStream out, AttributeSet a) throws IOException
~~~

## Parámetros
* **AttributeSet a**,  {% include w3api/param_description.html metodo=_data parametro="AttributeSet a" %}
* **ObjectOutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="ObjectOutputStream out" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[StyleContext](/Java/StyleContext/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StyleContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
