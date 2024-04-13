---
title: Utilities.getPositionBelow()
permalink: /Java/Utilities/getPositionBelow/
date: 2021-01-11
key: Java.U.Utilities
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.Utilities.metodos valor="getPositionBelow" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static int getPositionBelow(JTextComponent c, int offs, float x)
static int getPositionBelow(JTextComponent c, int offs, int x)
~~~

## Parámetros
* **float x**,  {% include w3api/param_description.html metodo=_dato parametro="float x" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **int offs**,  {% include w3api/param_description.html metodo=_dato parametro="int offs" %}
* **JTextComponent c**,  {% include w3api/param_description.html metodo=_dato parametro="JTextComponent c" %}

## Clase Padre
[Utilities](/Java/Utilities/)

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
