---
title: CommandAPDU.CommandAPDU()
permalink: Java/CommandAPDU/CommandAPDU
date: 2021-01-04
key: JavaJava.C.CommandAPDU
category: java
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
* **int apduLength**,  {% include w3api/param_description.html metodo=_data parametro="int apduLength" %}
* **byte[] data**,  {% include w3api/param_description.html metodo=_data parametro="byte[] data" %}
* **int dataLength**,  {% include w3api/param_description.html metodo=_data parametro="int dataLength" %}
* **int ins**,  {% include w3api/param_description.html metodo=_data parametro="int ins" %}
* **int p1**,  {% include w3api/param_description.html metodo=_data parametro="int p1" %}
* **int ne**,  {% include w3api/param_description.html metodo=_data parametro="int ne" %}
* **int cla**,  {% include w3api/param_description.html metodo=_data parametro="int cla" %}
* **ByteBuffer apdu**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer apdu" %}
* **byte[] apdu**,  {% include w3api/param_description.html metodo=_data parametro="byte[] apdu" %}
* **int apduOffset**,  {% include w3api/param_description.html metodo=_data parametro="int apduOffset" %}
* **int p2**,  {% include w3api/param_description.html metodo=_data parametro="int p2" %}
* **int dataOffset**,  {% include w3api/param_description.html metodo=_data parametro="int dataOffset" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CommandAPDU](/Java/CommandAPDU/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CommandAPDU.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
