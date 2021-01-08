---
title: FloatControl.shift()
permalink: Java/FloatControl/shift
date: 2021-01-04
key: JavaJava.F.FloatControl
category: java
tags: ['java se', 'javax.sound.sampled', 'java.desktop', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FloatControl.metodos valor="shift" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void shift(float from, float to, int microseconds)
~~~

## Parámetros
* **int microseconds**,  {% include w3api/param_description.html metodo=_data parametro="int microseconds" %}
* **float from**,  {% include w3api/param_description.html metodo=_data parametro="float from" %}
* **float to**,  {% include w3api/param_description.html metodo=_data parametro="float to" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[FloatControl](/Java/FloatControl/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FloatControl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
