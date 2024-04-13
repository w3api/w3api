---
title: SyncFactory.getRegisteredProviders()
permalink: /Java/SyncFactory/getRegisteredProviders/
date: 2021-01-11
key: Java.S.SyncFactory
category: Java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SyncFactory.metodos valor="getRegisteredProviders" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Enumeration<SyncProvider> getRegisteredProviders() throws SyncFactoryException
~~~

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
