---
title: KeyStoreSpi.engineGetEntry()
permalink: Java/KeyStoreSpi/engineGetEntry
date: 2021-01-04
key: JavaJava.K.KeyStoreSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStoreSpi.metodos valor="engineGetEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public KeyStore.Entry engineGetEntry(String alias, KeyStore.ProtectionParameter protParam) throws KeyStoreException, NoSuchAlgorithmException, UnrecoverableEntryException
~~~

## Parámetros
* **KeyStore.ProtectionParameter protParam**,  {% include w3api/param_description.html metodo=_data parametro="KeyStore.ProtectionParameter protParam" %}
* **String alias**,  {% include w3api/param_description.html metodo=_data parametro="String alias" %}

## Excepciones
[KeyStoreException](/Java/KeyStoreException/), [NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [UnrecoverableKeyException](/Java/UnrecoverableKeyException/), [UnrecoverableEntryException](/Java/UnrecoverableEntryException/)

## Clase Padre
[KeyStoreSpi](/Java/KeyStoreSpi/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyStoreSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
