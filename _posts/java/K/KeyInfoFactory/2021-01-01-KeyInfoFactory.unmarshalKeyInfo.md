---
title: KeyInfoFactory.unmarshalKeyInfo()
permalink: Java/KeyInfoFactory/unmarshalKeyInfo
date: 2021-01-11
key: JavaJava.K.KeyInfoFactory
category: java
tags: ['java se', 'javax.xml.crypto.dsig.keyinfo', 'java.xml.crypto', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyInfoFactory.metodos valor="unmarshalKeyInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract KeyInfo unmarshalKeyInfo(XMLStructure xmlStructure) throws MarshalException
~~~

## Parámetros
* **XMLStructure xmlStructure**,  {% include w3api/param_description.html metodo=_dato parametro="XMLStructure xmlStructure" %}

## Excepciones
[MarshalException](/Java/MarshalException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[KeyInfoFactory](/Java/KeyInfoFactory/)

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
