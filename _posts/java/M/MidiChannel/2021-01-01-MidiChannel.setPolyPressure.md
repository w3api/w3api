---
title: MidiChannel.setPolyPressure()
permalink: /Java/MidiChannel/setPolyPressure/
date: 2021-01-11
key: Java.M.MidiChannel
category: Java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MidiChannel.metodos valor="setPolyPressure" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setPolyPressure(int noteNumber, int pressure)
~~~

## Parámetros
* **int pressure**,  {% include w3api/param_description.html metodo=_dato parametro="int pressure" %}
* **int noteNumber**,  {% include w3api/param_description.html metodo=_dato parametro="int noteNumber" %}

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
