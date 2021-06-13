---
title: RemoteRef.invoke()
permalink: Java/RemoteRef/invoke
date: 2021-01-11
key: Java.R.RemoteRef
category: java
tags: ['java se', 'java.rmi.server', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RemoteRef.metodos valor="invoke" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object invoke(Remote obj, Method method, Object[] params, long opnum) throws Exception
@Deprecated void invoke(RemoteCall call) throws Exception
~~~

## Parámetros
* **Remote obj**,  {% include w3api/param_description.html metodo=_dato parametro="Remote obj" %}
* **Object[] params**,  {% include w3api/param_description.html metodo=_dato parametro="Object[] params" %}
* **long opnum**,  {% include w3api/param_description.html metodo=_dato parametro="long opnum" %}
* **RemoteCall call**,  {% include w3api/param_description.html metodo=_dato parametro="RemoteCall call" %}
* **Method method**,  {% include w3api/param_description.html metodo=_dato parametro="Method method" %}

## Excepciones
[Exception](/Java/Exception/)

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
