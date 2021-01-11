---
title: SyncFactory.setJNDIContext()
permalink: Java/SyncFactory/setJNDIContext
date: 2021-01-11
key: JavaJava.S.SyncFactory
category: java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SyncFactory.metodos valor="setJNDIContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setJNDIContext(Context ctx) throws SyncFactoryException
~~~

## Parámetros
* **Context ctx**,  {% include w3api/param_description.html metodo=_dato parametro="Context ctx" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [SyncFactoryException](/Java/SyncFactoryException/)

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
