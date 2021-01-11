---
title: CardChannel.transmit()
permalink: Java/CardChannel/transmit
date: 2021-01-11
key: JavaJava.C.CardChannel
category: java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardChannel.metodos valor="transmit" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract int transmit(ByteBuffer command, ByteBuffer response) throws CardException
public abstract ResponseAPDU transmit(CommandAPDU command) throws CardException
~~~

## Parámetros
* **ByteBuffer response**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer response" %}
* **CommandAPDU command**,  {% include w3api/param_description.html metodo=_dato parametro="CommandAPDU command" %}
* **ByteBuffer command**,  {% include w3api/param_description.html metodo=_dato parametro="ByteBuffer command" %}

## Excepciones
[CardException](/Java/CardException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CardChannel](/Java/CardChannel/)

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
