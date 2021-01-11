---
title: MidiChannel.programChange()
permalink: Java/MidiChannel/programChange
date: 2021-01-11
key: JavaJava.M.MidiChannel
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiChannel.metodos valor="programChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void programChange(int program)
void programChange(int bank, int program)
~~~

## Parámetros
* **int program**,  {% include w3api/param_description.html metodo=_dato parametro="int program" %}
* **int bank**,  {% include w3api/param_description.html metodo=_dato parametro="int bank" %}

## Clase Padre
[MidiChannel](/Java/MidiChannel/)

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
