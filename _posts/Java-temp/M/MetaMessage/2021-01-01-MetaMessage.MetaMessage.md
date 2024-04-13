---
title: MetaMessage.MetaMessage()
permalink: /Java/MetaMessage/MetaMessage/
date: 2021-01-11
key: Java.M.MetaMessage
category: Java
tags: ['java se', 'javax.sound.midi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MetaMessage.constructores valor="MetaMessage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MetaMessage()
protected MetaMessage(byte[] data)
public MetaMessage(int type, byte[] data, int length) throws InvalidMidiDataException
~~~

## Parámetros
* **byte[] data**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] data" %}
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[InvalidMidiDataException](/Java/InvalidMidiDataException/)

## Clase Padre
[MetaMessage](/Java/MetaMessage/)

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
