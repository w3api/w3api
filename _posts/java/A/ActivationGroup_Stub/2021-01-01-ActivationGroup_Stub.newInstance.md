---
title: ActivationGroup_Stub.newInstance()
permalink: /Java/ActivationGroup_Stub/newInstance/
date: 2021-01-11
key: Java.A.ActivationGroup_Stub
category: Java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationGroup_Stub.metodos valor="newInstance" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MarshalledObject newInstance(ActivationID id, ActivationDesc desc) throws RemoteException, ActivationException
~~~

## Parámetros
* **ActivationID id**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationID id" %}
* **ActivationDesc desc**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationDesc desc" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [RemoteException](/Java/RemoteException/)

## Clase Padre
[ActivationGroup_Stub](/Java/ActivationGroup_Stub/)

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
