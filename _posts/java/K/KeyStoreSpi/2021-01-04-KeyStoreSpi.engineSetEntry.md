---
title: KeyStoreSpi.engineSetEntry()
permalink: Java/KeyStoreSpi/engineSetEntry
date: 2021-01-04
key: JavaJava.K.KeyStoreSpi
category: java
tags: ['java se', 'java.security', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyStoreSpi.metodos valor="engineSetEntry" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void engineSetEntry(String alias, KeyStore.Entry entry, KeyStore.ProtectionParameter protParam) throws KeyStoreException
~~~

## Parámetros
* **KeyStore.Entry entry**,  {% include w3api/param_description.html metodo=_data parametro="KeyStore.Entry entry" %}
* **KeyStore.ProtectionParameter protParam**,  {% include w3api/param_description.html metodo=_data parametro="KeyStore.ProtectionParameter protParam" %}
* **String alias**,  {% include w3api/param_description.html metodo=_data parametro="String alias" %}

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
{%- for _ldc in site.data.Java.K.KeyStoreSpi.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
