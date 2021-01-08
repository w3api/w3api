---
title: CardTerminals.waitForChange()
permalink: Java/CardTerminals/waitForChange
date: 2021-01-04
key: JavaJava.C.CardTerminals
category: java
tags: ['java se', 'javax.smartcardio', 'java.smartcardio', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CardTerminals.metodos valor="waitForChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void waitForChange() throws CardException
public abstract boolean waitForChange(long timeout) throws CardException
~~~

## Parámetros
* **long timeout**,  {% include w3api/param_description.html metodo=_data parametro="long timeout" %}

## Excepciones
[CardException](/Java/CardException/), [IllegalStateException](/Java/IllegalStateException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[CardTerminals](/Java/CardTerminals/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CardTerminals.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
