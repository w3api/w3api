---
title: AlphaComposite.getInstance()
permalink: Java/AlphaComposite/getInstance
date: 2021-01-11
key: JavaJava.A.AlphaComposite
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AlphaComposite.metodos valor="getInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static AlphaComposite getInstance(int rule)
public static AlphaComposite getInstance(int rule, float alpha)
~~~

## Parámetros
* **float alpha**,  {% include w3api/param_description.html metodo=_dato parametro="float alpha" %}
* **int rule**,  {% include w3api/param_description.html metodo=_dato parametro="int rule" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[AlphaComposite](/Java/AlphaComposite/)

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
