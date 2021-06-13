---
title: ActivationGroup.ActivationGroup()
permalink: /Java/ActivationGroup/ActivationGroup/
date: 2021-01-11
key: Java.A.ActivationGroup
category: Java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationGroup.constructores valor="ActivationGroup" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected ActivationGroup(ActivationGroupID groupID) throws RemoteException
~~~

## Parámetros
* **ActivationGroupID groupID**,  {% include w3api/param_description.html metodo=_dato parametro="ActivationGroupID groupID" %}

## Excepciones
[RemoteException](/Java/RemoteException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ActivationGroup](/Java/ActivationGroup/)

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
