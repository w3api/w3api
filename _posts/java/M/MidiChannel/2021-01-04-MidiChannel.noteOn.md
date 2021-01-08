---
title: MidiChannel.noteOn()
permalink: Java/MidiChannel/noteOn
date: 2021-01-04
key: JavaJava.M.MidiChannel
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiChannel.metodos valor="noteOn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void noteOn(int noteNumber, int velocity)
~~~

## Parámetros
* **int velocity**,  {% include w3api/param_description.html metodo=_data parametro="int velocity" %}
* **int noteNumber**,  {% include w3api/param_description.html metodo=_data parametro="int noteNumber" %}

## Clase Padre
[MidiChannel](/Java/MidiChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MidiChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
