---
title: AWTKeyStroke.getAWTKeyStroke()
permalink: Java/AWTKeyStroke/getAWTKeyStroke
date: 2021-01-10
key: JavaJava.A.AWTKeyStroke
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AWTKeyStroke.metodos valor="getAWTKeyStroke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AWTKeyStroke getAWTKeyStroke(char keyChar)
public static AWTKeyStroke getAWTKeyStroke(int keyCode, int modifiers)
public static AWTKeyStroke getAWTKeyStroke(int keyCode, int modifiers, boolean onKeyRelease)
public static AWTKeyStroke getAWTKeyStroke(Character keyChar, int modifiers)
public static AWTKeyStroke getAWTKeyStroke(String s)
~~~

## Parámetros
* **char keyChar**,  {% include w3api/param_description.html metodo=_dato parametro="char keyChar" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **int keyCode**,  {% include w3api/param_description.html metodo=_dato parametro="int keyCode" %}
* **int modifiers**,  {% include w3api/param_description.html metodo=_dato parametro="int modifiers" %}
* **boolean onKeyRelease**,  {% include w3api/param_description.html metodo=_dato parametro="boolean onKeyRelease" %}
* **Character keyChar**,  {% include w3api/param_description.html metodo=_dato parametro="Character keyChar" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AWTKeyStroke](/Java/AWTKeyStroke/)

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
