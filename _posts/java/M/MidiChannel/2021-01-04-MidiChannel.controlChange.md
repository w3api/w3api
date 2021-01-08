---
title: MidiChannel.controlChange()
permalink: Java/MidiChannel/controlChange
date: 2021-01-04
key: JavaJava.M.MidiChannel
category: java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiChannel.metodos valor="controlChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void controlChange(int controller, int value)
~~~

## Parámetros
* **int value**,  {% include w3api/param_description.html metodo=_data parametro="int value" %}
* **int controller**,  {% include w3api/param_description.html metodo=_data parametro="int controller" %}

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
