---
title: CachedRowSet.acceptChanges()
permalink: Java/CachedRowSet/acceptChanges
date: 2021-01-04
key: JavaJava.C.CachedRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CachedRowSet.metodos valor="acceptChanges" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void acceptChanges() throws SyncProviderException
void acceptChanges(Connection con) throws SyncProviderException
~~~

## Parámetros
* **Connection con**,  {% include w3api/param_description.html metodo=_data parametro="Connection con" %}

## Excepciones
[SyncProviderException](/Java/SyncProviderException/)

## Clase Padre
[CachedRowSet](/Java/CachedRowSet/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CachedRowSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
