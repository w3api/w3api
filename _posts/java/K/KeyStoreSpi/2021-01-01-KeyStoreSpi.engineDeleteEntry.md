---
title: KeyStoreSpi.engineDeleteEntry()
permalink: Java/KeyStoreSpi/engineDeleteEntry
date: 2021-01-11
key: JavaJava.K.KeyStoreSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStoreSpi.metodos valor="engineDeleteEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void engineDeleteEntry(String alias) throws KeyStoreException
~~~

## Parámetros
* **String alias**,  {% include w3api/param_description.html metodo=_dato parametro="String alias" %}

## Excepciones
[KeyStoreException](/Java/KeyStoreException/)

## Clase Padre
[KeyStoreSpi](/Java/KeyStoreSpi/)

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
