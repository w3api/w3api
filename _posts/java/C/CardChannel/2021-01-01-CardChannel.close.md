---
title: CardChannel.close()
permalink: /Java/CardChannel/close/
date: 2021-01-11
key: Java.C.CardChannel
category: Java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardChannel.metodos valor="close" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void close() throws CardException
~~~

## Excepciones
[CardException](/Java/CardException/), [IllegalStateException](/Java/IllegalStateException/)

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
