---
title: AWTKeyStroke.getAWTKeyStroke()
permalink: Java/AWTKeyStroke/getAWTKeyStroke
date: 2021-01-04
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
* **char keyChar**,  {% include w3api/param_description.html metodo=_data parametro="char keyChar" %}
* **Character keyChar**,  {% include w3api/param_description.html metodo=_data parametro="Character keyChar" %}
* **int modifiers**,  {% include w3api/param_description.html metodo=_data parametro="int modifiers" %}
* **int keyCode**,  {% include w3api/param_description.html metodo=_data parametro="int keyCode" %}
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}
* **boolean onKeyRelease**,  {% include w3api/param_description.html metodo=_data parametro="boolean onKeyRelease" %}

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
{%- for _ldc in site.data.Java.A.AWTKeyStroke.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
