---
title: KeyStoreSpi.engineEntryInstanceOf()
permalink: Java/KeyStoreSpi/engineEntryInstanceOf
date: 2021-01-11
key: JavaJava.K.KeyStoreSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStoreSpi.metodos valor="engineEntryInstanceOf" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean engineEntryInstanceOf(String alias, Class<? extends KeyStore.Entry> entryClass)
~~~

## Parámetros
* **String alias**,  {% include w3api/param_description.html metodo=_dato parametro="String alias" %}
* **Class&lt;? extends KeyStore.Entry&gt; entryClass**,  {% include w3api/param_description.html metodo=_dato parametro="Class<? extends KeyStore.Entry> entryClass" %}

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
