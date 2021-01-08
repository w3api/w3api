---
title: KeyInfoFactory.newPGPData()
permalink: Java/KeyInfoFactory/newPGPData
date: 2021-01-04
key: JavaJava.K.KeyInfoFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig.keyinfo', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyInfoFactory.metodos valor="newPGPData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract PGPData newPGPData(byte[] keyId)
public abstract PGPData newPGPData(byte[] keyId, byte[] keyPacket, List<? extends XMLStructure> other)
public abstract PGPData newPGPData(byte[] keyPacket, List<? extends XMLStructure> other)
~~~

## Parámetros
* **List&lt;? extends XMLStructure&gt; other**,  {% include w3api/param_description.html metodo=_data parametro="List<? extends XMLStructure> other" %}
* **byte[] keyPacket**,  {% include w3api/param_description.html metodo=_data parametro="byte[] keyPacket" %}
* **byte[] keyId**,  {% include w3api/param_description.html metodo=_data parametro="byte[] keyId" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[KeyInfoFactory](/Java/KeyInfoFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyInfoFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
