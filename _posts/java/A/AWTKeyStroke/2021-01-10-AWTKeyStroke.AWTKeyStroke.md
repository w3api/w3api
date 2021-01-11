---
title: AWTKeyStroke.AWTKeyStroke()
permalink: Java/AWTKeyStroke/AWTKeyStroke
date: 2021-01-10
key: JavaJava.A.AWTKeyStroke
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AWTKeyStroke.constructores valor="AWTKeyStroke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected AWTKeyStroke()
protected AWTKeyStroke(char keyChar, int keyCode, int modifiers, boolean onKeyRelease)
~~~

## Parámetros
* **char keyChar**,  {% include w3api/param_description.html metodo=_dato parametro="char keyChar" %}
* **int modifiers**,  {% include w3api/param_description.html metodo=_dato parametro="int modifiers" %}
* **boolean onKeyRelease**,  {% include w3api/param_description.html metodo=_dato parametro="boolean onKeyRelease" %}
* **int keyCode**,  {% include w3api/param_description.html metodo=_dato parametro="int keyCode" %}

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
