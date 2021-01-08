---
title: SysexMessage.setMessage()
permalink: Java/SysexMessage/setMessage
date: 2021-01-04
key: JavaJava.S.SysexMessage
category: java
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
* **byte[] data**,  {% include w3api/param_description.html metodo=_data parametro="byte[] data" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int status**,  {% include w3api/param_description.html metodo=_data parametro="int status" %}

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
{%- for _ldc in site.data.Java.S.SysexMessage.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
