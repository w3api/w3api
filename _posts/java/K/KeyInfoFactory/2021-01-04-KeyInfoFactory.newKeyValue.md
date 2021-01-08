---
title: KeyInfoFactory.newKeyValue()
permalink: Java/KeyInfoFactory/newKeyValue
date: 2021-01-04
key: JavaJava.K.KeyInfoFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig.keyinfo', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyInfoFactory.metodos valor="newKeyValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract KeyValue newKeyValue(PublicKey key) throws KeyException
~~~

## Parámetros
* **PublicKey key**,  {% include w3api/param_description.html metodo=_data parametro="PublicKey key" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [KeyException](/Java/KeyException/)

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
