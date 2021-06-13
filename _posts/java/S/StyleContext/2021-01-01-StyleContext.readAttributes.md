---
title: StyleContext.readAttributes()
permalink: /Java/StyleContext/readAttributes/
date: 2021-01-11
key: Java.S.StyleContext
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StyleContext.metodos valor="readAttributes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void readAttributes(ObjectInputStream in, MutableAttributeSet a) throws ClassNotFoundException, IOException
~~~

## Parámetros
* **MutableAttributeSet a**,  {% include w3api/param_description.html metodo=_dato parametro="MutableAttributeSet a" %}
* **ObjectInputStream in**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectInputStream in" %}

## Excepciones
[ClassNotFoundException](/Java/ClassNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[StyleContext](/Java/StyleContext/)

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
