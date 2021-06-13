---
title: RemoteRef.done()
permalink: Java/RemoteRef/done
date: 2021-01-11
key: Java.R.RemoteRef
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RemoteRef.metodos valor="done" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated void done(RemoteCall call) throws RemoteException
~~~

## Parámetros
* **RemoteCall call**,  {% include w3api/param_description.html metodo=_dato parametro="RemoteCall call" %}

## Excepciones
[RemoteException](/Java/RemoteException/)

## Clase Padre
[RemoteRef](/Java/RemoteRef/)

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
