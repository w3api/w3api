---
title: CardChannel.transmit()
permalink: Java/CardChannel/transmit
date: 2021-01-04
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
* **CommandAPDU command**,  {% include w3api/param_description.html metodo=_data parametro="CommandAPDU command" %}
* **ByteBuffer response**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer response" %}
* **ByteBuffer command**,  {% include w3api/param_description.html metodo=_data parametro="ByteBuffer command" %}

## Excepciones
[CardException](/Java/CardException/), [ReadOnlyBufferException](/Java/ReadOnlyBufferException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CardChannel](/Java/CardChannel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CardChannel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
