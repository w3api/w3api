---
title: AWTKeyStroke.AWTKeyStroke()
permalink: Java/AWTKeyStroke/AWTKeyStroke
date: 2021-01-04
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
* **int keyCode**,  {% include w3api/param_description.html metodo=_data parametro="int keyCode" %}
* **char keyChar**,  {% include w3api/param_description.html metodo=_data parametro="char keyChar" %}
* **boolean onKeyRelease**,  {% include w3api/param_description.html metodo=_data parametro="boolean onKeyRelease" %}
* **int modifiers**,  {% include w3api/param_description.html metodo=_data parametro="int modifiers" %}

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
