---
title: SysexMessage.setMessage()
permalink: /Java/SysexMessage/setMessage/
date: 2021-01-11
key: Java.S.SysexMessage
category: Java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SysexMessage.metodos valor="setMessage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setMessage(byte[] data, int length) throws InvalidMidiDataException
public void setMessage(int status, byte[] data, int length) throws InvalidMidiDataException
~~~

## Parámetros
* **int status**,  {% include w3api/param_description.html metodo=_dato parametro="int status" %}
* **byte[] data**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] data" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[InvalidMidiDataException](/Java/InvalidMidiDataException/)

## Clase Padre
[SysexMessage](/Java/SysexMessage/)

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
