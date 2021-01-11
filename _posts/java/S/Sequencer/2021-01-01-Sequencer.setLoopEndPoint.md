---
title: Sequencer.setLoopEndPoint()
permalink: Java/Sequencer/setLoopEndPoint
date: 2021-01-11
key: JavaJava.S.Sequencer
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Sequencer.metodos valor="setLoopEndPoint" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setLoopEndPoint(long tick)
~~~

## Parámetros
* **long tick**,  {% include w3api/param_description.html metodo=_dato parametro="long tick" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Sequencer](/Java/Sequencer/)

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