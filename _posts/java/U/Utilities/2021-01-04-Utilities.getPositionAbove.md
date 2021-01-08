---
title: Utilities.getPositionAbove()
permalink: Java/Utilities/getPositionAbove
date: 2021-01-04
key: JavaJava.U.Utilities
category: java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.Utilities.metodos valor="getPositionAbove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static int getPositionAbove(JTextComponent c, int offs, float x)
static int getPositionAbove(JTextComponent c, int offs, int x)
~~~

## Parámetros
* **JTextComponent c**,  {% include w3api/param_description.html metodo=_data parametro="JTextComponent c" %}
* **float x**,  {% include w3api/param_description.html metodo=_data parametro="float x" %}
* **int offs**,  {% include w3api/param_description.html metodo=_data parametro="int offs" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Clase Padre
[Utilities](/Java/Utilities/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.Utilities.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
