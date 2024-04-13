---
title: RMIJRMPServerImpl.makeClient()
permalink: /Java/RMIJRMPServerImpl/makeClient/
date: 2021-01-11
key: Java.R.RMIJRMPServerImpl
category: Java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIJRMPServerImpl.metodos valor="makeClient" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected RMIConnection makeClient(String connectionId, Subject subject) throws IOException
~~~

## Parámetros
* **Subject subject**,  {% include w3api/param_description.html metodo=_dato parametro="Subject subject" %}
* **String connectionId**,  {% include w3api/param_description.html metodo=_dato parametro="String connectionId" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[RMIJRMPServerImpl](/Java/RMIJRMPServerImpl/)

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
