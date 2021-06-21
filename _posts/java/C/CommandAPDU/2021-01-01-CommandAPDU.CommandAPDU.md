---
title: CommandAPDU.CommandAPDU()
permalink: /Java/CommandAPDU/CommandAPDU/
date: 2021-01-11
key: Java.C.CommandAPDU
category: Java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CommandAPDU.constructores valor="CommandAPDU" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CommandAPDU(byte[] apdu)
public CommandAPDU(byte[] apdu, int apduOffset, int apduLength)
public CommandAPDU(int cla, int ins, int p1, int p2)
public CommandAPDU(int cla, int ins, int p1, int p2, byte[] data)
public CommandAPDU(int cla, int ins, int p1, int p2, byte[] data, int ne)
public CommandAPDU(int cla, int ins, int p1, int p2, byte[] data, int dataOffset, int dataLength)
public CommandAPDU(int cla, int ins, int p1, int p2, byte[] data, int dataOffset, int dataLength, int ne)
public CommandAPDU(int cla, int ins, int p1, int p2, int ne)
public CommandAPDU(ByteBuffer apdu)
~~~

## Parámetros
* **byte[] apdu**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] apdu" %}
* **int cla**,  {% include w3api/param_description.html metodo=_dato parametro="int cla" %}
* **int p1**,  {% include w3api/param_description.html metodo=_dato parametro="int p1" %}
* **int apduLength**,  {% include w3api/param_description.html metodo=_dato parametro="int apduLength" %}
* **int p2**,  {% include w3api/param_description.html metodo=_dato parametro="int p2" %}
* **int dataOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int dataOffset" %}
* **int dataLength**,  {% include w3api/param_description.html metodo=_dato parametro="int dataLength" %}
* **int apduOffset**,  {% include w3api/param_description.html metodo=_dato parametro="int apduOffset" %}
* **byte[] data**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] data" %}
* **int ne**,  {% include w3api/param_description.html metodo=_dato parametro="int ne" %}
* **ByteBuffer apdu**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer apdu" %}
* **int ins**,  {% include w3api/param_description.html metodo=_dato parametro="int ins" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CommandAPDU](/Java/CommandAPDU/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
