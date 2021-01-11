---
title: Sequencer.recordEnable()
permalink: Java/Sequencer/recordEnable
date: 2021-01-11
key: JavaJava.S.Sequencer
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Sequencer.metodos valor="recordEnable" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void recordEnable(Track track, int channel)
~~~

## Parámetros
* **int channel**,  {% include w3api/param_description.html metodo=_dato parametro="int channel" %}
* **Track track**,  {% include w3api/param_description.html metodo=_dato parametro="Track track" %}

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
