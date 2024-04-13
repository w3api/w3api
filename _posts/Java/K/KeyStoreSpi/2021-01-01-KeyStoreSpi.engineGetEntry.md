---
title: KeyStoreSpi.engineGetEntry()
permalink: /Java/KeyStoreSpi/engineGetEntry/
date: 2021-01-11
key: Java.K.KeyStoreSpi
category: Java
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
* **String alias**,  {% include w3api/param_description.html metodo=_dato parametro="String alias" %}
* **KeyStore.ProtectionParameter protParam**,  {% include w3api/param_description.html metodo=_dato parametro="KeyStore.ProtectionParameter protParam" %}

## Excepciones
[NoSuchAlgorithmException](/Java/NoSuchAlgorithmException/), [UnrecoverableEntryException](/Java/UnrecoverableEntryException/), [KeyStoreException](/Java/KeyStoreException/), [UnrecoverableKeyException](/Java/UnrecoverableKeyException/)

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
