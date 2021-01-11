---
title: RemoteRef.newCall()
permalink: Java/RemoteRef/newCall
date: 2021-01-11
key: JavaJava.R.RemoteRef
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RemoteRef.metodos valor="newCall" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated RemoteCall newCall(RemoteObject obj, Operation[] op, int opnum, long hash) throws RemoteException
~~~

## Parámetros
* **int opnum**,  {% include w3api/param_description.html metodo=_dato parametro="int opnum" %}
* **Operation[] op**,  {% include w3api/param_description.html metodo=_dato parametro="Operation[] op" %}
* **RemoteObject obj**,  {% include w3api/param_description.html metodo=_dato parametro="RemoteObject obj" %}
* **long hash**,  {% include w3api/param_description.html metodo=_dato parametro="long hash" %}

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
