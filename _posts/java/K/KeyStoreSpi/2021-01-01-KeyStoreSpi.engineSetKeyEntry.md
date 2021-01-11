---
title: KeyStoreSpi.engineSetKeyEntry()
permalink: Java/KeyStoreSpi/engineSetKeyEntry
date: 2021-01-11
key: JavaJava.K.KeyStoreSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStoreSpi.metodos valor="engineSetKeyEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void engineSetKeyEntry(String alias, byte[] key, Certificate[] chain) throws KeyStoreException
public abstract void engineSetKeyEntry(String alias, Key key, char[] password, Certificate[] chain) throws KeyStoreException
~~~

## Parámetros
* **Key key**,  {% include w3api/param_description.html metodo=_dato parametro="Key key" %}
* **byte[] key**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] key" %}
* **char[] password**,  {% include w3api/param_description.html metodo=_dato parametro="char[] password" %}
* **Certificate[] chain**,  {% include w3api/param_description.html metodo=_dato parametro="Certificate[] chain" %}
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
