---
title: SyncFactory.registerProvider()
permalink: /Java/SyncFactory/registerProvider/
date: 2021-01-11
key: Java.S.SyncFactory
category: Java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SyncFactory.metodos valor="registerProvider" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void registerProvider(String providerID) throws SyncFactoryException
~~~

## Parámetros
* **String providerID**,  {% include w3api/param_description.html metodo=_dato parametro="String providerID" %}

## Excepciones
[SyncFactoryException](/Java/SyncFactoryException/)

## Clase Padre
[SyncFactory](/Java/SyncFactory/)

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
