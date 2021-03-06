---
title: ShortMessage.setMessage()
permalink: /Java/ShortMessage/setMessage/
date: 2021-01-11
key: Java.S.ShortMessage
category: Java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.ShortMessage.metodos valor="setMessage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setMessage(int status) throws InvalidMidiDataException
public void setMessage(int status, int data1, int data2) throws InvalidMidiDataException
public void setMessage(int command, int channel, int data1, int data2) throws InvalidMidiDataException
~~~

## Parámetros
* **int status**,  {% include w3api/param_description.html metodo=_dato parametro="int status" %}
* **int channel**,  {% include w3api/param_description.html metodo=_dato parametro="int channel" %}
* **int data1**,  {% include w3api/param_description.html metodo=_dato parametro="int data1" %}
* **int data2**,  {% include w3api/param_description.html metodo=_dato parametro="int data2" %}
* **int command**,  {% include w3api/param_description.html metodo=_dato parametro="int command" %}

## Excepciones
[InvalidMidiDataException](/Java/InvalidMidiDataException/)

## Clase Padre
[ShortMessage](/Java/ShortMessage/)

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
