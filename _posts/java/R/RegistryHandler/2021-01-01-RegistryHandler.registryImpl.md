---
title: RegistryHandler.registryImpl()
permalink: /Java/RegistryHandler/registryImpl/
date: 2021-01-11
key: Java.R.RegistryHandler
category: Java
tags: ['java se', 'java.rmi.registry', 'java.rmi', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RegistryHandler.metodos valor="registryImpl" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated Registry registryImpl(int port) throws RemoteException
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}

## Excepciones
[RemoteException](/Java/RemoteException/)

## Clase Padre
[RegistryHandler](/Java/RegistryHandler/)

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
