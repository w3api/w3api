---
title: SyncProvider.setDataSourceLock()
permalink: /Java/SyncProvider/setDataSourceLock/
date: 2021-01-11
key: Java.S.SyncProvider
category: Java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SyncProvider.metodos valor="setDataSourceLock" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract void setDataSourceLock(int datasource_lock) throws SyncProviderException
~~~

## Parámetros
* **int datasource_lock**,  {% include w3api/param_description.html metodo=_dato parametro="int datasource_lock" %}

## Excepciones
[SyncProviderException](/Java/SyncProviderException/)

## Clase Padre
[SyncProvider](/Java/SyncProvider/)

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
